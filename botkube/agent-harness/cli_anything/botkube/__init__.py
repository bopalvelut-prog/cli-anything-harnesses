import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('BotKube running')
@cli.command()
def notify(): click.echo('BotKube notifications')
if __name__ == '__main__': cli()
