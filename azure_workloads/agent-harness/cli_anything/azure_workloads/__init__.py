import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_workloads running')
@cli.command()
def start(): click.echo('azure_workloads started')
if __name__ == '__main__': cli()
