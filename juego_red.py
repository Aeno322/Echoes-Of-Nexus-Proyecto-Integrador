
import socket
import sys

from net import Net, PUERTO, POS_HOST, POS_CLIENTE


def obtener_ip_local():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def conectar(rol, ip_dest=""):
    if rol == "1":
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind(("0.0.0.0", PUERTO))
        servidor.listen(1)
        print(f"Esperando jugador... Tu IP: {obtener_ip_local()} Puerto: {PUERTO}")
        canal, _ = servidor.accept()
        servidor.close()
        return canal
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(5)
    cliente.connect((ip_dest.split(":")[0], PUERTO))
    cliente.settimeout(None)
    return cliente


def main():
    if len(sys.argv) > 1:
        rol = sys.argv[1]
        ip_dest = sys.argv[2] if len(sys.argv) > 2 else ""
    else:
        rol = input("¿Qué eres? (1 = Servidor / 2 = Cliente): ").strip()
        ip_dest = input("IP del servidor: ").strip() if rol == "2" else ""
    canal = conectar(rol, ip_dest)
    net = Net(canal, rol=rol)
    pos = POS_HOST if rol == "1" else POS_CLIENTE
    from main import Game
    game = Game(net=net, player_pos=pos, mode='pvp', rol=rol)
    try:
        game.run()
    finally:
        net.cerrar()


if __name__ == "__main__":
    main()
