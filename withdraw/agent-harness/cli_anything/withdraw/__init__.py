import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('withdraw running')
@cli.command()
def start(): click.echo('withdraw started')
if __name__ == '__main__': cli()
