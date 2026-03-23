import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dump running')
@cli.command()
def start(): click.echo('dump started')
if __name__ == '__main__': cli()
