import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('greenplum running')
@cli.command()
def start(): click.echo('greenplum started')
if __name__ == '__main__': cli()
