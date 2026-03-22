import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def bot(): click.echo('Discord bot started')
@cli.command()
def webhook(): click.echo('Discord webhook')
if __name__ == '__main__': cli()
