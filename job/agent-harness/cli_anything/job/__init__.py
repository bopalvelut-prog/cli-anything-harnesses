import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('job running')
@cli.command()
def start(): click.echo('job started')
if __name__ == '__main__': cli()
