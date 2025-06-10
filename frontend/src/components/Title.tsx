import { useState } from 'react';
import axios from 'axios';

type Props = {
	setMessages: any;
};

const Title = ({ setMessages }: Props) => {
	const [isResseting, setIsRessetting] = useState(false);

	// Reset Conversation
	const resetConversation = async () => {
		setIsRessetting(true);

		await axios
			.get('http://localhost:8000/reset')
			.then((res) => {
				if (res.status === 200) {
					setMessages([]);
				} else {
					console.error('There was an error with the axios call');
				}
			})
			.catch((error) => {
				console.error(error);
			});
		setIsRessetting(false);
	};

	return (
		<div>
			<div className="flex justify-between items-center w-full p-4 bg-gray-900 text-white shadow font-bold">
				<div className="italic">Sarah - SWE Interview Bot</div>
				<button
					onClick={resetConversation}
					className={
						'transition-all duration-300 text-blue-300 hover:text-pink-500 ' +
						(isResseting && 'animate-pulse')
					}
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						className="w-6 h-6"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"
						/>
					</svg>
				</button>
			</div>
		</div>
	);
};

export default Title;
