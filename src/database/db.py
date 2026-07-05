
from src.database.config import supabase
import bcrypt

def check_teacher_exists(username):
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0

def create_teacher(username,password,name) :
    