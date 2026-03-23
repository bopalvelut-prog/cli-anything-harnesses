import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scatter running')
@cli.command()
def start(): click.echo('scatter started')
if __name__ == '__main__': cli()
