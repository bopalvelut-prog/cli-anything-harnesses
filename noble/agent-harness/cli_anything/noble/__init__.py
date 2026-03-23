import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('noble running')
@cli.command()
def start(): click.echo('noble started')
if __name__ == '__main__': cli()
