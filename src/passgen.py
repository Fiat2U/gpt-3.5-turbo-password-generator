import openai
import config


def generate_password(length=10):
    openai.api_key = config.OPENAI_API_KEY

    try:
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'user', 'content': f'Please generate a password with ${length} characters'}
            ]
        )

        return completion.choices[0].message.content.strip()
    except Exception as e:
        print(e)
        return False
    finally:
        print('Done!')


if __name__ == '__main__':
    password = generate_password()
    print(password)
