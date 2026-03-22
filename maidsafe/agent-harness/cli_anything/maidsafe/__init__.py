import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('MaidSafe status')
if __name__ == '__main__': cli()
