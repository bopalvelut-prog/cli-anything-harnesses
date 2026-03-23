import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dialog running')
@cli.command()
def start(): click.echo('dialog started')
if __name__ == '__main__': cli()
