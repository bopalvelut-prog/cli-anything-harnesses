import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('noise running')
@cli.command()
def start(): click.echo('noise started')
if __name__ == '__main__': cli()
