import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pool running')
@cli.command()
def start(): click.echo('pool started')
if __name__ == '__main__': cli()
