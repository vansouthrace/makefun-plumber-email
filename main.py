import os

ENTRY = "Subject: Your evenings back: bookkeeping for busy plumbers\n\nHi, I'm Sam from ClearBooks. Your week runs on call-outs, quotes and parts runs, then the invoices wait until 9pm. We take the paperwork off plumbers: invoices sent, receipts filed, late payers chased, and your tax return done, all for $49 a month with no contract. Your customers already trust you with their homes; the books should be just as easy. We handle VAT too, and send one clear monthly summary you can read in two minutes. One plumber we help got six hours a week back. I'll set you up in one 20-minute call, and if it doesn't save you time, walk away. Can I ring you Tuesday at 7pm for ten minutes? Thanks, Sam"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
