import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('verify running')
@cli.command()
def start(): click.echo('verify started')
if __name__ == '__main__': cli()
