import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('typical running')
@cli.command()
def start(): click.echo('typical started')
if __name__ == '__main__': cli()
