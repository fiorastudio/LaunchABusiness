import sys
import json

def calculate_cagr(beginning_value, ending_value, years):
    try:
        bv = float(beginning_value)
        ev = float(ending_value)
        n = float(years)
        
        if bv <= 0:
            return {"error": "Beginning value must be greater than zero."}
            
        cagr = ((ev / bv) ** (1 / n)) - 1
        
        return {
            "beginning_value": bv,
            "ending_value": ev,
            "years": n,
            "cagr_percent": round(cagr * 100, 2),
            "multiplier": round(ev / bv, 2)
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 cagr_calc.py <beginning_value> <ending_value> <years>")
        sys.exit(1)
        
    result = calculate_cagr(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(result, indent=2))
