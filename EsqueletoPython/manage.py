import  os
import json
import time
from app.services.region_all_service import RegionAllService

def main():
    print("llego aca")
    RegionAllService().create_region()
    return True

if __name__ == "__main__":
    main()