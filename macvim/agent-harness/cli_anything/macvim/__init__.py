import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('macvim running')
@cli.command()
def start(): click.echo('macvim started')
if __name__ == '__main__': cli()
