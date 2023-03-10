import pytest
import asyncio
from src.passgen import generate_password


@pytest.mark.asyncio
async def test_generate_password_length():
    password_length = 15
    password = await asyncio.wait_for(generate_password(length=password_length), timeout=10)
    assert isinstance(password, str)
    assert len(password) == password_length


@pytest.mark.asyncio
async def test_generate_password_characters():
    password = await asyncio.wait_for(generate_password(), timeout=10)
    assert any(char.isdigit() for char in password)
    assert any(char.isalpha() for char in password)
    assert any(char.islower() for char in password)
    assert any(char.isupper() for char in password)


@pytest.mark.asyncio
async def test_generate_password_invalid_length():
    # result = await asyncio.wait_for(generate_password(length=5), timeout=10)
    result = await generate_password(5)
    assert isinstance(result, bool)
    assert result is False
