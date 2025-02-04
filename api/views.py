import json
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def classify_number(request):
    num_str = request.GET.get('number')
    if num_str is None:
        return JsonResponse({"error": True, "message": "Missing 'number' parameter."}, status=400)
    
    try:
        number = int(num_str)
    except ValueError:
        return JsonResponse({"number": num_str, "error": True}, status=400)
    

    is_prime = check_prime(number)
    is_perfect = check_perfect(number)
    is_armstrong = check_armstrong(number)
    digit_sum = sum(int(digit) for digit in str(abs(number)))  # sum of digits
    
   
    if is_armstrong:
        properties = ["armstrong", "odd" if number % 2 != 0 else "even"]
    else:
        properties = ["odd"] if number % 2 != 0 else ["even"]
    
    #fun fact from Numbers api
    fun_fact = get_fun_fact(number)
    
    #response
    response_data = {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact,
    }
    
    return JsonResponse(response_data, status=200)


def check_prime(n):
    if n < 2:
        return False
  
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_perfect(n):
    if n < 2:
        return False
    divisors = [1]
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors) == n


def check_armstrong(n):

    if n < 0:
        return False
    digits = str(n)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    return armstrong_sum == n


def get_fun_fact(n):

    url = f"http://numbersapi.com/{n}/math?json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Return the text from the API
            return data.get("text", f"No fun fact found for {n}.")
        else:
            return f"No fun fact found for {n}."
    except requests.RequestException:
        return f"Unable to retrieve fun fact for {n} at this time."