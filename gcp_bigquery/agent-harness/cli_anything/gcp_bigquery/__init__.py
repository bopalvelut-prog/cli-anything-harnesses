import click
@click.group()
def cli(): pass
@cli.command()
def query(): click.echo('BigQuery query')
@cli.command()
def datasets(): click.echo('BigQuery datasets')
if __name__ == '__main__': cli()
