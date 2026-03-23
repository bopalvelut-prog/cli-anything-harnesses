import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unique running')
@cli.command()
def start(): click.echo('unique started')
if __name__ == '__main__': cli()
