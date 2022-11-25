from pathlib import Path

from tkinter import Tk
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkmsg

def first_gui() -> None:
    root = Tk()    
    root.lift()
    root.attributes("-alpha",0)
    root.protocol("WM_DELETE_WINDOW",(lambda: "pass")())

def massage_info(msg:str) -> None:
    """情報表示

    Args:
        msg (str): 表示させたい文字列
    """
    tkmsg.showinfo(title="info",message=msg)

def warning(msg: str) -> None:
    """警告表示

    Args:
        msg (str): 警告で表示させたい文字列
    """
    tkmsg.showwarning(title="warnig",message=msg)

def retry(msg: str) -> bool:
    """再試行

    Args:
        msg (str): 再試行で表示させたい文字列

    Returns:
        bool: 再試行の有無
    """
    retry = tkmsg.askokcancel(title="info",message=msg)
    return retry

def error(error: str,msg: str) -> None:
    """エラー表示

    Args:
        error (str): エラータイトル
        msg (str): エラー文
    """
    tkmsg.showerror(title=error,message=msg)

def choose_directry() -> str:
    """ディレクトリの選択

    Returns:
        str: 選択したディレクトリのパス
    """
    tkmsg.showinfo(
        title="info",message="choose a drectory"
    )
    current_dir = Path().absolute()
    dir_path = tkfd.askdirectory(initialdir=current_dir)

    return dir_path

def choose_file() -> str:
    """ファイルの選択

    Returns:
        str: 選択したファイルのパス
    """
    tkmsg.showinfo(
        title="info",message="choose a file"
    )
    current_dir = Path().absolute()
    file_path = tkfd.askopenfilename(initialdir=current_dir)
    return file_path
    