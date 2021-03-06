
from .. import udB

try:
    eval(udB.get("WARNS"))
except BaseException:
    udB.set("WARNS", "{}")


def add_warn(chat, user, count, reason):
    x = eval(udB.get("WARNS"))
    try:
        x[chat].update({user: [count, reason]})
    except BaseException:
        x.update({chat: {user: [count, reason]}})
    return udB.set("WARNS", str(x))


def warns(chat, user):
    x = eval(udB.get("WARNS"))
    try:
        count, reason = x[chat][user][0], x[chat][user][1]
        return count, reason
    except BaseException:
        return 0, None


def reset_warn(chat, user):
    x = eval(udB.get("WARNS"))
    try:
        x[chat].pop(user)
        return udB.set("WARNS", str(x))
    except BaseException:
        return
