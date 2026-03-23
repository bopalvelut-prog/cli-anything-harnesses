import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grafana_mimir running')
@cli.command()
def start(): click.echo('grafana_mimir started')
if __name__ == '__main__': cli()
