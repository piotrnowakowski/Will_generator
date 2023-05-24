
# Will Generation AI

This project uses OpenAI's GPT-4, Flask, jQuery and Bootstrap to generate segments of a legal will based on user inputs. The AI is using  a set of wills and user-answered questions to create a will document that is as close as possible to the user's intentions.

The application provides a simple user interface for selecting different segments of a will (such as "Personal Information", "Executor", etc.) and generates the corresponding segment based on user's answered questions and examples from other wills.

## Installation

To get started, clone this repository to your local machine:

    `git clone https://github.com/piotrnowakowski/Will_generator.git`

Navigate into the directory:

    `cd will-generation-ai`

Install the required dependencies:

    `pip install -r requirements.txt`

## Usage

Start the Flask server:

bashCopy code

    `python generate_will.py`

You can then navigate to `http://localhost:5000` in your web browser to use the application.
You also have to provide Your own openai API key. Default location is openai_api.txt file.

## Discussion

This project presents a few challenges. The most prominent one is the segmentation of wills. While we have a list of questions pertaining to different segments of a will, the wills themselves may not necessarily be segmented in the same way. To tackle this, I used the GPT-4 model to split the wills into the distinctive chapters as mentioned in those questions. This allowed us to reference the style of these segments and generate corresponding sections of a new will.

However, even with GPT-4, generating a complete will in one go proved difficult due to the complexity of legal wills and the nuances in different segments. As such, we opted to generate individual segments based on user input and stitch them together to form a complete will.

## Future Development

There are several areas for future development to enhance the capabilities of the AI:

1. Improve segmentation of wills: While the AI currently does a decent job at segmenting wills, there's still room for improvement. We can use more refined models or techniques to segment the wills even more accurately.
2. Format recognition: Recognize and maintain the formatting of wills, for a more seamless and coherent output.
3. Implement a database of wills: Store wills as embeddings with metadata such as associated questions or the content of the will chapter. This would allow for quick search and retrieval of relevant segments for enhancing the generation prompts.
4. Direct prompting of GPT to modify segments: Allow users to directly prompt GPT to change specific segments of the will, giving the user more control over the output.
5. Generate final document: Instead of displaying the generated will segments in a text area, we could allow users to generate a final document (e.g., a PDF file) with all the completed chapters.

## Conclusion

This project demonstrates the potential of AI in assisting with complex legal tasks like generating a will. Despite the challenges, with the power of GPT-4, we were able to build an AI that generates segments of a will based on user inputs and examples. As AI technology continues to evolve, we expect its capabilities in this area to only get better.
