import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('impact running')
@cli.command()
def start(): click.echo('impact started')
if __name__ == '__main__': cli()
