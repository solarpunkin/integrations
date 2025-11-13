import React, { useState, useRef, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import './Chat.css';

const Chat = () => {
    const [message, setMessage] = useState('');
    const [chatHistory, setChatHistory] = useState([]);
    const [image, setImage] = useState(null);
    const fileInputRef = useRef();
    const location = useLocation();
    const { transcript, listening, resetTranscript } = useSpeechRecognition();

    useEffect(() => {
        if (transcript) {
            setMessage(transcript);
        }
    }, [transcript]);

    const handleSendMessage = async () => {
        if (!message && !image) return;

        let newChatHistory = [...chatHistory];
        if (message) {
            newChatHistory.push({ sender: 'user', message });
        }
        if (image) {
            newChatHistory.push({ sender: 'user', image: URL.createObjectURL(image) });
        }
        
        setChatHistory(newChatHistory);
        setMessage('');
        setImage(null);
        resetTranscript();

        const payload = { message, currentPage: location.pathname };
        if (image) {
            const reader = new FileReader();
            reader.readAsDataURL(image);
            reader.onloadend = async () => {
                const base64data = reader.result;
                payload.image_data = base64data.split(',')[1];
                const response = await fetch('/api/agent', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(payload),
                });
                const data = await response.json();
                setChatHistory([...newChatHistory, { sender: 'movi', message: data.response }]);
            };
        } else {
            const response = await fetch('/api/agent', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload),
            });
            const data = await response.json();
            setChatHistory([...newChatHistory, { sender: 'movi', message: data.response }]);
        }
    };

    const handleImageChange = (e) => {
        setImage(e.target.files[0]);
    };

    return (
        <div className="chat-container">
            <div className="chat-history">
                {chatHistory.map((chat, index) => (
                    <div key={index} className={`chat-message ${chat.sender}`}>
                        {chat.message && typeof chat.message === 'string' && <div>{chat.message}</div>}
                        {chat.message && typeof chat.message === 'object' && !Array.isArray(chat.message) && <div>{chat.message.text}</div>}
                        {chat.message && Array.isArray(chat.message) && chat.message.map((item, i) => (
                            <div key={i}>{item.text}</div>
                        ))}
                        {chat.image && <img src={chat.image} alt="upload" />}
                    </div>                ))}
            </div>
            <div className="chat-input">
                <input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                />
                <input 
                    type="file" 
                    accept="image/*" 
                    onChange={handleImageChange} 
                    ref={fileInputRef} 
                    style={{display: 'none'}} 
                />
                <button onClick={() => fileInputRef.current.click()}>Upload</button>
                <button onClick={SpeechRecognition.startListening}>
                    {listening ? 'Listening...' : 'Speak'}
                </button>
                <button onClick={handleSendMessage}>Send</button>
            </div>
        </div>
    );
};

export default Chat;
