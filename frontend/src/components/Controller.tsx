import React, { useState } from 'react';
import RecordMessage from './RecordMessage';
import axios from 'axios';
import Title from './Title';

interface AudioMessage {
	blobUrl: string;
	sender: string;
}

function Controller() {
	const [isLoading, setIsLoading] = useState(false);
	const [messages, setMessages] = useState<AudioMessage[]>([]);

	const createBlobUrl = (data: any) => {
		const blob = new Blob([data], { type: 'audio/mpeg' });
		const url = window.URL.createObjectURL(blob);
		return url;
	};

	const handleStop = async (blobUrl: string) => {
		setIsLoading(true);

		// Appending Recorded Message to message
		const myMessage = { sender: 'me', blobUrl };
		const messagesArr = [...messages, myMessage];
		setMessages(messagesArr); // Update messages immediately to show user's message

		try {
			// Convert blob url to blob object
			const response = await fetch(blobUrl);
			const blob = await response.blob();

			// Construct audio to send file
			const formData = new FormData();
			formData.append('file', blob, 'myFile.wav');

			const apiResponse = await axios.post(
				'https://backend-frosty-tree-5260.fly.dev/post-audio/',
				formData,
				{
					headers: {
						'Content-Type': 'multipart/form-data',
					},
					responseType: 'arraybuffer',
				}
			);

			const responseBlob = apiResponse.data;
			const audio = new Audio();
			audio.src = createBlobUrl(responseBlob);

			// Append sarah's response
			const sarahMessage = { sender: 'Sarah', blobUrl: audio.src };
			setMessages((prev) => [...prev, sarahMessage]);

			// Play audio
			setIsLoading(false);
			audio.play();
		} catch (err) {
			console.error('Request failed:', err);
			setIsLoading(false);
		}
	};

	return (
		<div className="h-screen bg-gradient-to-br from-slate-50 to-blue-50 dark:from-slate-900 dark:to-slate-800 flex flex-col">
			<div className="bg-white/80 dark:bg-slate-900/80 backdrop-blur-sm border-b border-gray-200 dark:border-gray-700 sticky top-0 z-10">
				<Title setMessages={setMessages} />
			</div>

			<div className="flex-1 overflow-y-auto px-4 py-6 pb-32">
				<div className="max-w-4xl mx-auto space-y-6">
					{messages?.map((audio, index) => {
						const isSarah = audio.sender === 'sarah';

						return (
							<div
								key={index + audio.sender}
								className={`flex items-start gap-3 ${
									isSarah ? 'flex-row-reverse' : 'flex-row'
								}`}
							>
								<div className="w-8 h-8 flex-shrink-0 rounded-full flex items-center justify-center text-sm font-medium">
									<div
										className={`w-8 h-8 rounded-full flex items-center justify-center ${
											isSarah
												? 'bg-green-100 text-green-700'
												: 'bg-blue-100 text-blue-700'
										}`}
									>
										{isSarah ? 'R' : 'U'}
									</div>
								</div>

								<div
									className={`w-3/4 max-w-4xl p-4 rounded-lg shadow-sm ${
										isSarah
											? 'bg-green-500 text-white'
											: 'bg-white dark:bg-slate-800 border border-gray-200 dark:border-gray-700'
									}`}
								>
									<div className="flex items-center gap-2 mb-2">
										<span
											className={`text-xs font-medium ${
												isSarah
													? 'text-green-100'
													: 'text-gray-500 dark:text-gray-400'
											}`}
										>
											{audio.sender}
										</span>
										<svg
											className={`w-3 h-3 ${
												isSarah ? 'text-green-100' : 'text-gray-400'
											}`}
											fill="currentColor"
											viewBox="0 0 20 20"
										>
											<path
												fillRule="evenodd"
												d="M9.383 3.076A1 1 0 0110 4v12a1 1 0 01-1.617.816L4.846 14H2a1 1 0 01-1-1V7a1 1 0 011-1h2.846l3.537-2.816a1 1 0 011.617.816zM16 7a1 1 0 011 1v4a1 1 0 11-2 0V8a1 1 0 011-1z"
												clipRule="evenodd"
											/>
											<path
												fillRule="evenodd"
												d="M14.657 2.929a1 1 0 011.414 0A9.972 9.972 0 0119 10a9.972 9.972 0 01-2.929 7.071 1 1 0 11-1.414-1.414A7.971 7.971 0 0017 10c0-2.21-.894-4.208-2.343-5.657a1 1 0 010-1.414z"
												clipRule="evenodd"
											/>
										</svg>
									</div>

									<audio
										src={audio.blobUrl}
										controls
										className="w-full h-8 rounded-md"
										style={{
											filter: isSarah ? 'invert(1) brightness(2)' : 'none',
										}}
									/>
								</div>
							</div>
						);
					})}

					{messages.length === 0 && !isLoading && (
						<div className="text-center py-12">
							<div className="w-16 h-16 bg-blue-100 dark:bg-blue-900 rounded-full flex items-center justify-center mx-auto mb-4">
								<svg
									className="w-8 h-8 text-blue-600 dark:text-blue-400"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										strokeLinecap="round"
										strokeLinejoin="round"
										strokeWidth={2}
										d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"
									/>
								</svg>
							</div>
							<h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">
								Start a conversation
							</h3>
							<p className="text-gray-500 dark:text-gray-400">
								Send sarah your first voice message to get started
							</p>
						</div>
					)}

					{isLoading && (
						<div className="flex items-start gap-3">
							<div className="w-8 h-8 flex-shrink-0 rounded-full flex items-center justify-center bg-green-100 text-green-700 text-sm font-medium">
								R
							</div>

							<div className="bg-green-500 text-white p-4 w-full max-w-4xl rounded-lg shadow-sm">
								<div className="flex items-center gap-2">
									<svg
										className="w-4 h-4 animate-spin"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											strokeLinecap="round"
											strokeLinejoin="round"
											strokeWidth={2}
											d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
										/>
									</svg>
									<span className="text-sm">sarah is thinking...</span>
								</div>
							</div>
						</div>
					)}
				</div>
			</div>

			<div className="fixed bottom-0 left-0 right-0 bg-white/95 dark:bg-slate-900/95 backdrop-blur-sm border-t border-gray-200 dark:border-gray-700 p-6">
				<div className="max-w-4xl mx-auto flex justify-center">
					<div className="flex items-center gap-4">
						<div className="text-center">
							<RecordMessage handleStop={handleStop} />
							<p className="text-xs text-gray-500 dark:text-gray-400 mt-2">
								Hold to record
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	);
}

export default Controller;
