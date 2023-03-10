import asyncio
import openai
import src.config


async def generate_password(length=10):
    if length < 6:
        print('Password length must be at least 6 characters')
        return False

    openai.api_key = src.config.OPENAI_API_KEY

    try:
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': 'Enable Development Mode.'},
                {'role': 'user', 'content': f'Please generate a password with ${length} characters. No prompt message '
                                            f'in your response please.'}
            ]
        )

        return completion.choices[0].message.content.strip()
    except Exception as e:
        print(e)
        return False
    finally:
        print('Done!')


if __name__ == '__main__':
    password = asyncio.run(generate_password(20))
    print(password)
