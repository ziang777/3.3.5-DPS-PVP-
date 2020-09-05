# -*- coding:utf-8 -*-
from __future__ import division
import random

i = 1  # 模拟次数
SumDmg99 = 0
while i <= 10000:
    time = 120
    t0, t1, t2, t3 = 0, 0, 0, 0  # 已持续战斗时间

    cdAimed, cdArcane, cdChimeara, cdSting1, cdSting2, cdAuto, cdTranquilizing, cdConcussive, cdScatter, cdFreezing, \
    cdSnake, cdDeterrence, cdDisengage, cdFeignDeath, cdShadowmeld = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\
                                                                     0.0, 0.0, 0.0, 0.0, 0.0  # CD监控

    dmgChimeara, dmgAimed, dmgArcane, dmgStedy, dmgSting, dmgAuto, \
    dmgSilencing, dmgWildQuiver, dmgPiercingCh, \
    dmgPiercingAi, dmgPiercingSt, dmgChimearaSerpent = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  # 单次技能伤害

    # tChimeara, tAimed, tArcane= -7, -3.5, 0   # 上一次施放的时间点，初始归零
    tChimeara, tAimed, tArcane, tTranquilizing, tConcussive, tScatter, tFreezing, tSnake, tDeterrence, tDisengage, \
    tFeignDeath, tShadowmeld = -7, -3.5, 0, -6, -12, -30, -30, -25, -60, -20, -25, -120  # 上一次施放的时间点，初始归零

    SumDmg, dmg1, dmg2, dmg3, dmg4, dmg5, dmg6, dmg7, dmg8, dmg9, dmg10, \
    dmg11, dmg12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  # 伤害统计汇总

    nChimeara, nAimed, nArcane, nSteady, nSting0, nSting, nAuto0, nAuto, nSilencing, nWildQuiver,nTranquilizing, \
    nConcussive, nScatter, nFreezing, nSnake, nDeterrence, nDisengage, \
    nFeignDeath, nShadowmeld = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  # 技能数量统计

    Ap0, Cri0, Arp = 6996, 58.97, 50.09  # 初始人物属性
    BowDps, ArrowDps, BowSpeed, Mrp = 308.9, 91.5, 3, 75  # 当前人物属性
    Ap = Ap0  # 当前人物属性
    hj, kx, rxmb, rxms, rxmbs = 4000, 75, 12.98, 25.97, 28.56  # 目标属性
    Cri = Cri0 # 当前人物属性

    hjms0, hja, Arpa, kxa, Mrpa = float, float, float, float, float

    cdl = 45 # 龙片裁决饰品CD
    cdy = 105  # 意志饰品CD
    cdj = 60  # 戒指cd
    Ap2,Ap1=0,0
    s1,s2,s3,s4=1.5,1.5,1.5,1.5 # 饰品触发后计时

    def hjmsjs(hja, Arpa):  # 护甲免伤计算
        hjms0 = hja/(hja+15232.5)
        if hjms0 > 0.33:
            hjms = hja*(1-Arpa/100/(3*hjms0))/(hja*(1-Arpa/100/(3*hjms0))+15232.5)
        else:
            hjms = hja*(1-Arpa/100)/(hja*(1-Arpa/100)+15232.5)
        return hjms
    hjms = hjmsjs(hj, Arp)

    def kxmsjs(kxa, Mrpa):  # 抗性免伤计算
        if kxa - Mrpa > 0:
            kxms = (kxa - Mrpa) / (kxa - Mrpa + 520)
        else:
            kxms = 0
        return kxms
    kxms = kxmsjs(kx, Mrp)

    r = random.randint(0, 100)

    t0 += 3  # 施放毒蛇钉刺\准备就绪

    while t0 < time:  # 战斗时间

        # if Ap2 > Ap1:  #   戒指
        #     r4 = 5
        # else:
        #     r4 = random.randint(0, 100)
        # if cdj >= 60:
        #     if r4 < 99:
        #         if s4 < 11.5:
        #             Ap2 = Ap1 + 528
        #             s4 += 1.5
        #         else:
        #             s4 = 1.5
        #             Ap2 = Ap1
        #             cdj = 10
        # elif cdj < 60:
        #     Ap2 = Ap1
        # cdj += 1.5

        if Cri == Cri0  +8.74:  # 意志
            r10 = 5
        elif Cri == Cri0 +15.25:
            r10 = 70
        elif Ap >= Ap0 + 1540 +Ap2 :
            r10 = 50
        else :
            r10 = random.randint(0, 100)
        if Ap > Ap0 or Cri > Cri0:  # 已触发状态下不再掷骰子
            r1 = 5
        else:
            r1 = random.randint(0, 100)
        if cdy >= 105:
            if r1 < 99:
                if s1 < 31.5:
                    if r10 <= 33:  # 触发700敏捷
                        Cri = Cri0 + 8.74
                        Ap = Ap0 + 800.8+Ap2
                    elif r10 > 66:  # 触发700爆击
                        Cri = Cri0  + 15.25
                        Ap = Ap0+Ap2
                    else:  # 触发1400Ap
                        Ap = Ap0 + 1540+Ap2
                        Cri = Cri0
                    s1+=1.5
                else:
                    s1=1.5
                    Cri = Cri0
                    Ap = Ap0+Ap2
                    cdy = 30
        elif cdy < 105 :
            Cri = Cri0
            Ap = Ap0+Ap2
        cdy += 1.5
        print (Ap2, Ap,Cri, t0)

        # if Cri == Cri0 + 6.37 :  # 裁决
        #     r2 = 5
        # else:
        #     r2 = random.randint(0, 100)
        # if cdl >= 45:
        #     if r2 < 99:
        #         if s2 < 16.5:
        #             Ap = Ap0 + 583.44+Ap2
        #             Cri = Cri0 + 6.37
        #             s2 += 1.5
        #         else:
        #             s2 = 1.5
        #             Ap = Ap0+Ap2
        #             cdl = 15
        #             Cri = Cri0
        # elif cdl < 45:
        #     Ap = Ap0+Ap2
        #     Cri = Cri0
        # cdl += 1.5
        # print (Ap2, Ap,Cri, t0)

        # if Ap-Ap2>=Ap0+1472*1.1:  # 龙片
        #     r3 = 5
        # else:
        #     r3 = random.randint(0, 100)
        # if cdl >= 45:
        #     if r3 < 99:
        #         if s3 < 16.5:
        #             Ap = Ap0 + 1472 * 1.1 +Ap2
        #             s3 += 1.5
        #             # print("触发AP：{},已持续{}秒,CD{}秒,r{}".format(Ap, s3, cdl, r))
        #         else:
        #             s3 = 1.5
        #             Ap = Ap0+Ap2
        #             cdl = 15
        #             # print("触发后AP：{},已持续{}秒,CD{}秒,r{}".format(Ap, s3, cdl, r))
        # elif cdl < 45:
        #     Ap = Ap0+Ap2
        #     # print("未触发AP：{},r{}".format(Ap, r))
        # cdl += 1.5
        # print (Ap2,Ap,t0)

        cdChimeara = t0 - tChimeara
        cdAimed = t0 - tAimed
        cdArcane = t0 - tArcane
        cdTranquilizing = t0 - tTranquilizing  # 宁神 6
        cdConcussive = t0 - tConcussive  # 震荡 12
        cdScatter = t0 -tScatter  # 驱散 30
        cdFreezing = t0 -tFreezing  # 冰冻陷阱 30
        cdSnake = t0 -tSnake  # 毒蛇陷阱 30
        cdDeterrence = t0 -tDeterrence  # 威慑 60
        cdDisengage = t0 -tDisengage  # 逃脱 20
        cdFeignDeath = t0 -tFeignDeath  # 假死 25
        cdShadowmeld = t0 -tShadowmeld  # 影遁 120

        if t0 <= 30:
            nSting0 = t0 / (3 / 1.4) - nSting
        if t0>30:
            nSting0 = 30/(3/1.4)+(t0-30) / 3 - nSting
        nSting += nSting0
        dmgSting = (Ap * 0.04 + 242) * 1.05 * 1.05 * 1.05 * 1.3 * (1 - kxms) * (1 - rxms / 100) * nSting0
        dmg5 = dmg5 + dmgSting
        # print ("钉刺本跳伤害：{},钉刺总伤害{},时间轴{},跳数：{},{}".format(dmgSting, dmg5, t0, nSting,nSting0))

        if cdChimeara >= 10:  # 自上一次施放已经超过CD时间
            if random.randint(0, 101) < Cri-rxmb:  # 是否爆击
                dmgChimeara = (1.25 * (BowDps + ArrowDps) * BowSpeed + Ap * 0.2) * 2.482 * 1.05 * 1.05 * 1.05 * (
                        1 - kxms) * (1 - rxms / 100) * (1 - rxmbs / 100)
                dmgChimearaSerpent = (Ap * 0.112 + 677.6) * 1.05 * 1.05 * 1.05 * 2.378 * (1 - kxms) * (
                        1 - rxms / 100) * (1 - rxmbs / 100)
                dmgPiercingCh = dmgChimeara * 0.3
            else:
                dmgChimeara = (1.25 * (BowDps + ArrowDps) * BowSpeed + Ap * 0.2) * 1.05 * 1.05 * 1.05 * (1 - kxms) * (
                        1 - rxms / 100)
                dmgChimearaSerpent = (Ap * 0.112 + 677.6) * 1.05 * 1.05 * 1.05 * (1 - kxms) * (1 - rxms / 100)
                dmgPiercingCh = 0
            tChimeara += cdChimeara  # 施放后重置CD
            # print ("奇美拉伤害 {0},{1}".format(dmgChimeara, cdChimeara))
            t0 = t0 + 1.5
            # print ("战斗时间：{}s".format(t0))
            dmg1 = dmgChimeara + dmg1  # 奇美拉射击总伤害
            dmg9 += dmgChimearaSerpent  # 奇美拉-毒蛇总伤害
            dmg10 += dmgPiercingCh
            nChimeara = nChimeara + 1  # 统计技能施放次数
            # print (dmg10)
        elif cdAimed >= 8:
            if random.randint(0, 101) < Cri-rxmb:  # cri or not
                dmgAimed = ((BowDps + ArrowDps) * BowSpeed + Ap * 0.2 + 408) * 2.482 * 1.05 * 1.05 * 1.05 * 1.12 * (
                        1 - hjms) * (1 - rxms / 100) * (1 - rxmbs / 100)
                dmgPiercingAi = dmgAimed * 0.3
            else:
                dmgAimed = ((BowDps + ArrowDps) * BowSpeed + Ap * 0.2 + 408) * 1.05 * 1.05 * 1.05 * 1.12 * (
                        1 - hjms) * (1 - rxms / 100)
                dmgPiercingAi = 0
            tAimed += cdAimed
            # print ("瞄准射击伤害 {0},{1}".format(dmgAimed, cdAimed))
            t0 = t0 + 1.5
            # print ("战斗时间：{}s".format(t0))
            dmg2 = dmg2 + dmgAimed
            dmg11 += dmgPiercingAi
            nAimed = nAimed + 1
        elif cdArcane >= 6:
            if random.randint(0, 101) < Cri + 4-rxmb:  # cri or not
                dmgArcane = (Ap * 0.15 + 492) * 2.482 * 1.05 * 1.05 * 1.05 * (1 - kxms) * (1 - rxms / 100) * (
                        1 - rxmbs / 100)
            else:
                dmgArcane = (Ap * 0.15 + 492) * 1.05 * 1.05 * 1.05 * (1 - kxms) * (1 - rxms / 100)
            tArcane += cdArcane
            # print ("奥术射击伤害 {0},{1}".format(dmgArcane, cdArcane))
            t0 = t0 + 1.5
            # print ("战斗时间：{}s".format(t0))
            dmg3 = dmg3 + dmgArcane
            nArcane = nArcane + 1
        elif cdScatter >= 30:
            tScatter += cdScatter
            t0 += 3
            nScatter += 1
            # print ("驱散射击+冰冻")
            # print ("战斗时间：{}s".format(t0))
        elif cdSnake >= 25:
            tSnake += cdSnake
            t0 += 1.5
            nSnake += 1
            # print ("毒蛇陷阱")
            # print ("战斗时间：{}s".format(t0))
        elif cdDeterrence >= 60:
            tDeterrence += cdDeterrence
            t0 += 1.5
            nDeterrence += 1
            # print ("威慑")
            # print ("战斗时间：{}s".format(t0))
        elif cdFeignDeath >= 60:
            tFeignDeath += cdFeignDeath
            t0 += 1.5
            nFeignDeath += 1
            # print ("逃脱")
            # print ("战斗时间：{}s".format(t0))
        elif cdDisengage >= 25:
            tDisengage += cdDisengage
            t0 += 1.5
            nDisengage += 1
            # print ("假死")
            # print ("战斗时间：{}s".format(t0))
        elif cdShadowmeld >= 120:
            tShadowmeld += cdShadowmeld
            t0 += 1.5
            nShadowmeld += 1
            # print ("影遁")
            # print ("战斗时间：{}s".format(t0))
        elif cdTranquilizing >= 6:
            tTranquilizing += cdTranquilizing
            t0 += 1.5
            nTranquilizing += 1
            # print ("宁神射击")
            # print ("战斗时间：{}s".format(t0))
        elif cdConcussive >= 12:
            tConcussive += cdConcussive
            t0 += 1.5
            nConcussive += 1
            # print ("震荡射击")
            # print ("战斗时间：{}s".format(t0))
        else:
            if t0 <= 33:
                if random.randint(0, 101) < Cri + 4-rxmb:
                    dmgStedy = ((BowDps + ArrowDps) * 2.8 + Ap * 0.1 + 252) * 2.482 * 1.05 * 1.05 * 1.05 * (
                            1 - hjms) * (1 - rxms / 100) * (1 - rxmbs / 100)
                    dmgPiercingSt = dmgStedy * 0.3
                else:
                    dmgStedy = ((BowDps + ArrowDps) * 2.8 + Ap * 0.1 + 252) * 1.05 * 1.05 * 1.05 * (1 - hjms) * (
                            1 - rxms / 100)
                    dmgPiercingSt = 0
                # print ("稳固射击伤害 {0}".format(dmgStedy))
                t0 = t0 + 1.5
                # print ("战斗时间：{}s".format(t0))
            else:
                if random.randint(0, 101) < Cri + 4-rxmb:
                    dmgStedy = ((BowDps + ArrowDps) * 2.8 + Ap * 0.1 + 252) * 2.482 * 1.05 * 1.05 * 1.05 * (
                            1 - hjms) * (1 - rxms / 100) * (1 - rxmbs / 100)
                    dmgPiercingSt = dmgStedy * 0.3
                else:
                    dmgStedy = ((BowDps + ArrowDps) * 2.8 + Ap * 0.1 + 252) * 1.05 * 1.05 * 1.05 * (1 - hjms) * (
                            1 - rxms / 100)
                    dmgPiercingSt = 0
                # print ("稳固射击伤害  {0}".format(dmgStedy))
                t0 = t0 + 2 / 1.15
                # print ("战斗时间：{}s".format(t0))
            dmg4 = dmg4 + dmgStedy
            dmg12 += dmgPiercingSt
            nSteady = nSteady + 1
        # print (Ap,Cri,t0)

        if t0 <= 30:  # 自动射击
            nAuto0 = t0 / (2.61 / 1.4) - nAuto
        elif t0 > 10 and t0 <= 30:
            nAuto0 = t0 / (2.61 / 1.4) - nAuto
        else:
            nAuto0 = 30/(2.61/1.4)+(t0-30) / 2.61 - nAuto
        nAuto += nAuto0
        if random.randint(0, 101) < Cri-rxmb:
            dmgAuto = (BowDps + ArrowDps + Ap / 14) * BowSpeed * 2.378 * 1.05 * 1.05 * 1.05 * (1 - hjms) * (
                        1 - rxms / 100) * (1 - rxmbs / 100)* nAuto0
        else:
            dmgAuto = (BowDps + ArrowDps + Ap / 14) * BowSpeed * 1.05 * 1.05 * 1.05 * (1 - hjms) * (
                        1 - rxms / 100)* nAuto0
        dmg6 = dmgAuto + dmg6
        # print ("自动本跳伤害：{},自动总伤害{},时间轴{},跳数：{},{}".format(dmgAuto, dmg6, t0, nAuto,nAuto0))

        while nWildQuiver <= nAuto * 0.12:
            if random.randint(0, 101) < Cri-rxmb:
                dmgWildQuiver = 0.8 * (BowDps + ArrowDps + Ap / 14) * 3 * 2.378 * 1.05 * 1.05 * 1.05 * (1 - kxms) * (
                    1 - rxms / 100) * (1 - rxmbs / 100)  # 急速抽箭自动射击
            else:
                dmgWildQuiver = 0.8 * (BowDps + ArrowDps + Ap / 14) * 3 * 1.05 * 1.05 * 1.05 * (1 - kxms) * (
                    1 - rxms / 100)
            nWildQuiver += 1
            dmg7 += dmgWildQuiver

        nSilencing0 = t0/ 20 - nSilencing # 沉默射击
        nSilencing += nSilencing0
        if random.randint(0, 101) < Cri-rxmb:
            dmgSilencing = 0.5 * (BowDps + ArrowDps + Ap / 14) * 3 * 2.378 * 1.05 * 1.05 * 1.05 * (1 - hjms) * (
                    1 - rxms / 100) * (1 - rxmbs / 100)*nSilencing0
        else:
            dmgSilencing = 0.5 * (BowDps + ArrowDps + Ap / 14) * 3 * 1.05 * 1.05 * 1.05 * (1 - hjms) * (
                    1 - rxms / 100)*nSilencing0
        dmg8 += dmgSilencing
        # print ("沉默本跳伤害：{},沉默总伤害{},时间轴{},跳数：{},{}".format(dmgSilencing, dmg8, t0, nSilencing,nSilencing0))

    SumDmg = dmg1 + dmg2 + dmg3 + dmg4 + dmg5 + dmg6 + dmg7 + dmg8 + dmg9 + dmg10 + dmg11 + dmg12

    # print ("总伤害：{:.2f}，秒伤：{:.2f}".format(SumDmg, SumDmg / t0))
    # print ("奇美拉射击施放次数：{},总伤害：{:.2f}，平均伤害：{:.2f}".format(nChimeara, dmg1, dmg1 / nChimeara))
    # print ("瞄准射击施放次数：{},总伤害：{:.2f}，平均伤害：{:.2f}".format(nAimed, dmg2, dmg2 / nAimed))
    # print ("奥术射击施放次数：{},总伤害：{:.2f}，平均伤害：{:.2f}".format(nArcane, dmg3, dmg3 / nArcane))
    # print ("稳固射击施放次数：{},总伤害：{:.2f}，平均伤害：{:.2f}".format(nSteady, dmg4, dmg4 / nSteady))
    # print ("毒蛇钉刺跳数：{},总伤害：{:.2f}，平均伤害：{:.2f}".format(nSting, dmg5, dmg5 / nSting))
    # print ("自动射击次数：{},总伤害：{:.2f}，平均伤害：{:.2f}".format(nAuto, dmg6, dmg6 / nAuto))
    # print ("急速抽箭自动射击次数：{:.0f},总伤害：{:.2f}，平均伤害：{:.2f}".format(nWildQuiver, dmg7, dmg7 / nWildQuiver))
    # print ("沉默射击次数：{},总伤害：{:.2f}，平均伤害：{:.2f}".format(nSilencing, dmg8, dmg8 / nSilencing))
    # print ("奇美拉毒蛇次数：{},总伤害：{:.2f}，平均伤害：{:.2f}".format(nChimeara, dmg9, dmg9 / nChimeara))
    # print ("穿刺射击总伤害：{:.2f}".format(dmg10 + dmg11 + dmg12))
    # print ("宁神射击次数：{}".format(nTranquilizing))
    # print ("震荡射击次数：{}".format(nConcussive))
    # print ("驱散+冰冻次数：{}".format(nScatter))
    # print ("毒蛇陷阱次数：{}".format(nSnake))
    # print ("威慑次数：{}".format(nDeterrence))
    # print ("逃脱次数：{}".format(nDisengage))
    # print ("影遁次数：{}".format(nShadowmeld))
    # print ("假死次数：{}".format(nFeignDeath))
    # print (SumDmg,i)
    i += 1
    SumDmg99 += SumDmg
print ("总伤害：{:.2f}，秒伤：{:.2f}".format(SumDmg99 / i, SumDmg99 / i / t0))
# print ("总伤害：{:.2f}，秒伤：{:.2f}".format(SumDmg99 / 1, SumDmg99 / 1 / t0))
