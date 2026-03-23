import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('agora running')
@cli.command()
def start(): click.echo('agora started')
if __name__ == '__main__': cli()
