import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ohmyzsh running')
@cli.command()
def start(): click.echo('ohmyzsh started')
if __name__ == '__main__': cli()
