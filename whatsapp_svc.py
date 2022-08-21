from pywhatkit import whats
from pywhatkit.core import core

SCREEN_POS_DUAL_MONITOR_BOTTOM_RIGHT = (core.WIDTH/1.25, core.HEIGHT/1.5)

def test_msg_factory():
    num = "+5533999414145"
    msg_queue = []
    for preco in range(1, 11):
        msg_queue.append(
            {
                "number": num,
                "text": (
                    f"  *[Relatório de divisão de gastos]*\n"
                    f"Hola, você e mais 4 pessoas dividiram uma casquinha\n"
                    f"O total ficou R${preco},00 e a sua parte ficou R$0,40\n"
                    f"\n"
                    f"Pagar pix: https://linkpix.com.br"
                )
            }
        )

    return msg_queue


def send_msgs(queue, screen_pos):
    # Sempre abre nova aba na ultima janela chrome clicada
    # screen_pos: posicao da tela em que a janela vai abrir
    for msg in queue:
        whats.sendwhatmsg_instantly(
            phone_no=msg["number"],
            message=msg["text"],
            wait_time=10,
            tab_close=True,
            close_time=1,
            screen_pos=screen_pos
        )


msg_queue = test_msg_factory()
send_msgs(queue=msg_queue, screen_pos=SCREEN_POS_DUAL_MONITOR_BOTTOM_RIGHT)


# group_id = "LuSrodWhGcg4bU4u9Yhk4s"
# msg = """*[Relatório de divisão de gastos]*
# Hola, você e mais 4 pessoas dividiram uma casquinha
# O total ficou R$2,00 e a sua parte ficou R$0,40

# Pagar pix: https://linkpix.com.br"""
# msg = "Oi, isso é um teste ç _ç_ *ç* ~ç~"

# whats.sendwhatmsg_to_group_instantly(
#     group_id=group_id,
#     message=msg,
#     tab_close=True,
#     close_time=8
# )
