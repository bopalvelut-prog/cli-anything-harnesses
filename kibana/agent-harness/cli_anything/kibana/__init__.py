import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Kibana running on :5601')
@cli.command()
def plugins(): click.echo('Installed plugins')
if __name__ == '__main__': cli()
