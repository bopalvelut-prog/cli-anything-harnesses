import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Replit start')
@cli.command()
def deploy(): click.echo('Replit deploy')
if __name__ == '__main__': cli()
