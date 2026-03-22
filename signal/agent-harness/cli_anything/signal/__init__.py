
import click, requests, os
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Signal CLI available')
@cli.command()
@click.argument('recipient')
@click.argument('message')
def send(recipient, message): click.echo(f'Send to {recipient}: {message}')
if __name__ == '__main__': cli()
