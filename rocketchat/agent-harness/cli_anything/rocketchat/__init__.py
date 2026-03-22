import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def channels(): click.echo('Rocket.Chat channels')
@cli.command()
def send(): click.echo('Rocket.Chat message')
if __name__ == '__main__': cli()
