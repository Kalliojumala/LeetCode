/* 
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2**31, 2**31 − 1]. 

For this problem, if the quotient is strictly greater than 2**31 - 1, then return 2**31 - 1, and if the quotient is strictly less than -2**31, then return -2**31.

Constraints:

    -2**31 <= dividend, divisor <= 2**31 - 1
    divisor != 0
*/



const divideWithoutMulDivMod = (dividend, divisor) => {
    let result = 0;
    let isNegative = false;

    switch(true) {

        case (dividend < 0 && divisor > 0):
            dividend = Math.abs(dividend)
            isNegative = true
            break;

        case (dividend > 0 && divisor < 0):
            divisor = Math.abs(divisor)
            isNegative = true
            break;

        case (dividend < 0 && divisor < 0):
            dividend = Math.abs(dividend)
            divisor = Math.abs(divisor)
            break;

        default:
            break;
    }
    
    if(divisor === 1 && dividend >= 2147483647) {
        if(isNegative ) {
            return -2147483648
        }
        else {
            return 2147483647
        }
    }

    while(dividend >= divisor) {
        result += 1
        dividend = (dividend - divisor)
    }

    return isNegative ? Math.max(-2147483647 , -result) : Math.min(2147483647 ,result)
    
}

x = -2147483647

y = 1
console.log(divideWithoutMulDivMod(x,y))
