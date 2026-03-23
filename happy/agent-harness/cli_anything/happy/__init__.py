import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('happy running')
@cli.command()
def start(): click.echo('happy started')
if __name__ == '__main__': cli()
