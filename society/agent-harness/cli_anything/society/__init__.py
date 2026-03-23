import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('society running')
@cli.command()
def start(): click.echo('society started')
if __name__ == '__main__': cli()
