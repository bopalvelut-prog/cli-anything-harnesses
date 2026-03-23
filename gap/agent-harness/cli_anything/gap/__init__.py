import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gap running')
@cli.command()
def start(): click.echo('gap started')
if __name__ == '__main__': cli()
