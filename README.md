# Voice-Activated AI Chat System

This project is a sophisticated voice-activated chat system that leverages state-of-the-art AI for real-time conversation. It listens to spoken input through a microphone, transcribes the speech to text using the Vosk library, generates responses with the LlamaCpp model, and then speaks back the response using pyttsx3, creating a seamless conversational experience.

## Key Features

- **Real-Time Voice Recognition**: Transcribes spoken language into text in real-time.
- **Intelligent Conversation**: Uses the advanced LlamaCpp model to generate contextually relevant and engaging responses.
- **Audible Feedback**: Converts the AI's text responses back into speech, simulating a natural conversation.

## Prerequisites

- A high-quality microphone and a quiet environment are essential for capturing clear voice inputs.
- Python 3.x installed on your system.

## Software and Library Dependencies

- **sounddevice**: For capturing audio data in real-time.
- **numpy**: Processes the audio data for recognition.
- **vosk**: An offline speech recognition toolkit that supports various languages and accents.
- **LlamaCpp**: Provides the AI model for generating responses.
- **pyttsx3**: Converts text responses back into speech.
- **torch**: Necessary for running the LlamaCpp model.

## Installation

1. Install the required libraries with pip:

```bash
pip install sounddevice numpy vosk pyttsx3 torch


    Download and configure the Vosk speech recognition model from Vosk Model List. Choose a model compatible with your language and accent.

    Obtain the LlamaCpp model file suitable for conversational AI and ensure it's accessible to the script.

Setup

    Update model_path to your Vosk model directory.
    Set llama_model_path to the location of your LlamaCpp model file.
    Confirm your microphone is correctly set up as the default recording device. Adjust the script if using a specific device.

Running the System

Execute the script to start the voice chat:


python llama_vosk_Voice_chatbot.py

Speak into the microphone after you see "Listening..." on the console. The system will process your speech, generate a response, and read it aloud.
Usage Notes

    Response times may vary (~5 seconds on average) depending on the input complexity and system performance.
    The system is designed for short, concise responses. Customize the maximum response length as needed.
    High-quality microphones significantly improve transcription accuracy and overall experience.
    The conversation history is utilized to provide context to the AI, making responses more relevant.

Contributing

Contributions are welcome! If you have ideas for new features, improvements, or have found bugs, feel free to fork this repository, make changes, and submit a pull request.


Licensing Strategy for Personal and Commercial Use of Software
Introduction

In the evolving landscape of software development, striking a balance between open accessibility for personal use and monetizing commercial applications is a critical challenge for developers. This document outlines a licensing strategy designed to permit personal use of software freely while regulating commercial usage through explicit permissions or licensing agreements.
Licensing Overview

The proposed strategy involves a hybrid approach, combining elements of custom licensing and dual licensing models. This approach aims to maximize the software's accessibility and usability for non-commercial, personal projects while establishing a clear, legal framework for commercial exploitation.
Custom Licensing for Personal Use

A custom license can be crafted to explicitly allow personal, non-commercial use of the software under specified conditions. These conditions may include limitations on modifications, distribution, and use in commercial projects. The license would clearly state that:

    The software is available for personal, non-commercial use, granting users the rights to use, modify, and distribute the software with certain restrictions aimed at preventing commercial exploitation.
    Any use of the software in a commercial context requires obtaining a commercial license.

Commercial Licensing

For commercial users, a separate commercial license must be obtained. This license would outline the terms under which the software can be used commercially, potentially including a fee structure, support terms, updates, and any other relevant conditions. The commercial license aims to provide businesses with the flexibility and security needed for commercial use while compensating the developers for their work.
Implementation Steps
Drafting the Licenses

The first step involves drafting two sets of license terms: one for personal use and another for commercial use. It is recommended to consult with legal professionals to ensure that the licenses are enforceable, compliant with applicable laws, and clear to end-users.
Documentation and Communication

The licensing terms should be clearly documented and communicated through the software's official channels, such as the README file, the project's website, and within the software itself. This ensures that users are immediately aware of the licensing conditions and know how to proceed if they wish to use the software commercially.
Establishing Contact Procedures

A straightforward and accessible procedure for inquiring about and obtaining a commercial license should be established. This could include providing a contact email, a form on the project's website, or any other method that facilitates easy communication between commercial users and the developers.
Considerations
Legal Advice

Obtaining legal advice is crucial in drafting effective and enforceable licenses. This ensures that the licensing strategy is robust against potential legal challenges and compliant with international software law standards.
Community Reaction

Developers should be mindful of the open-source community's preferences for standard licensing models. Custom or restrictive licenses may impact the project's adoption, contribution levels, and overall community support.
Enforcement

Consideration should be given to the enforcement of the license terms, particularly in preventing unauthorized commercial use. Developers should establish mechanisms to monitor and address violations in a manner that is both effective and respectful of the software community.
Conclusion

By adopting a dual licensing strategy that differentiates between personal and commercial use, developers can foster a supportive environment for personal projects while creating a sustainable revenue stream from commercial applications. This approach respects the principles of open-source software while recognizing the value of the developers' efforts and the commercial potential of their work.