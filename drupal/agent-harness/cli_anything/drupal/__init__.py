import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Drupal status')
@cli.command()
def modules(): click.echo('Drupal modules')
if __name__ == '__main__': cli()
