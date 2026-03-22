import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def notify(): click.echo('Alchemy notification')
@cli.command()
def webhooks(): click.echo('Alchemy webhooks')
if __name__ == '__main__': cli()
