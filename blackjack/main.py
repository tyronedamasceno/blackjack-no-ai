from constants import DEALER_HIT_CONSTRAINT
from deck import Shoe
from game import Dealer, Player

player = Player()
dealer = Dealer()
shoe = Shoe()

print('Welcome to casino!')
print('Dealer is burning the first card')
shoe.draw()

while True:
    player.hand.clear()
    dealer.hand.clear()
    print(f'Current balance: {player.balance}')
    bet = float(input('Please, place your bet: '))
    player.balance -= bet

    player.hand.add_card(shoe.draw())
    dealer.hand.add_card(shoe.draw())
    player.hand.add_card(shoe.draw())
    dealer.hand.add_card(shoe.draw())

    print('Your hand:')
    player.hand.show()
    print("Dealer's hand:")
    dealer.hand.show(hide_first=True)

    if player.hand.is_blackjack:
        if dealer.hand.is_blackjack:
            print("You and dealer have blackjack, it's a push!")
            player.balance += bet
            continue
        print(f'You have blackjack! You win {bet + bet * 1.5}')
        player.balance += bet + bet * 1.5  # blackjack pays 3/2
        continue
    if dealer.hand.is_blackjack:
        print('Dealer has blackjack, you lost. Better luck next time')

    action = None
    while action != 'S':
        action = input(
            """
            What action do you want to take?

            Hit: H
            Double down: D
            Stand: S
        Your action:"""
        )
        if action == 'H':
            player.hand.add_card(shoe.draw())
            print('Your hand:')
            player.hand.show()
            if player.hand.is_busted:
                break
        if action == 'D':
            player.hand.add_card(shoe.draw())
            player.hand.show()
            player.balance -= bet
            bet += bet
            break

    if player.hand.is_busted:
        print('You busted! Better luck next time')
        continue

    print("Dealer's hand")
    dealer.hand.show()
    # Dealer must hit while has < 17, this rules can vary at each casino
    while dealer.hand.value < DEALER_HIT_CONSTRAINT:
        dealer.hand.add_card(shoe.draw())
        print('Dealer hits:')
        dealer.hand.show()

    if dealer.hand.is_busted or player.hand.value > dealer.hand.value:
        print(f'You win {bet + bet}')
        player.balance += bet + bet
    elif player.hand.value == dealer.hand.value:
        print("It's a push!")
        player.balance += bet
    elif player.hand.value < dealer.hand.value:
        print('You lost. Better luck next time')
