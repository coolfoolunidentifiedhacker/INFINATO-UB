

import { Composer } from 'telegraf';
import { closeConnection, leaveVc } from '../tgcalls';

export const exitVcHandler = Composer.action('exitVc', async ctx => {
    const chat = ctx.callbackQuery.message?.chat;

    if (!chat) {
        await ctx.answerCbQuery("Invalid Request");
        return false;
    }

    if (chat.type !== 'supergroup') {
        await ctx.answerCbQuery("Invalid Request");
        return false;
    }

    closeConnection();
    leaveVc(chat.id);
    await ctx.answerCbQuery("Leaving Voicechat");
})

export const exitCommand = Composer.command('exitVc', async ctx => {
    const { chat } = ctx.message;

    if (chat.type !== 'supergroup') {
        return;
    }

    closeConnection();
    leaveVc(chat.id);
    await ctx.reply("Left Voice Chat.");
})
