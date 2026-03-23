import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('poet running')
@cli.command()
def start(): click.echo('poet started')
if __name__ == '__main__': cli()
